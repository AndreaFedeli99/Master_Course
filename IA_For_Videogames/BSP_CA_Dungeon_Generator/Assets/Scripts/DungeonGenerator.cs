using System.Collections.Generic;
using UnityEditor;
using UnityEngine;

public class DungeonGenerator : MonoBehaviour
{
    public int randomSeed = 0;
    public int numberOfRooms = 20;
    public int borderSize = 5;

    public float roomFillRate = 0.4f;
    public float corridorFillRate = 0.15f;

    public bool drawBSP = false;
    public bool drawRooms = false;
    public bool drawCorridors = false;

    public void GenerateDungeon()
    {
        bsp = new BSP(new RectSpaceArea(0, WIDTH, 0, HEIGHT));
        bsp.BuildBSP(numberOfRooms - 1, MIN_SPLIT_PERCENTAGE, MAX_SPLIT_PERCENTAGE);

        rooms = new List<RectSpaceArea>();
        corridors = new List<RectSpaceArea>();

        map = new CellType[WIDTH, HEIGHT];
        InitMap();

        CreateRooms();
        CreateCorridors();

        SetCorridorBorderCells();

        foreach (var leaf in bsp.GetLeaves())
        {
            ApplyAutomata(leaf.value, NUMBER_OF_ITERATIONS);
        }

        GenerateMapMesh();
    }

    public static bool IsCellActive(CellType cell)
    {
        return cell == CellType.Wall || cell == CellType.CorridorBorderWall;
    }

    // Start is called before the first frame update
    void Start()
    {
        if (randomSeed == 0)
            randomSeed = (int)System.DateTime.Now.Ticks;
        Random.InitState(randomSeed);
    }

    private void OnDrawGizmos()
    {
        if (bsp != null && drawBSP)
        {
            Gizmos.color = Color.red;
            bsp.DrawBSP();
        }

        if (rooms != null && drawRooms)
        {
            Gizmos.color = Color.blue;
            foreach (RectSpaceArea area in rooms)
            {
                foreach (Edge edge in area.GetEdges())
                    Gizmos.DrawLine(edge.from, edge.to);
            }
        }

        if (corridors != null && drawCorridors)
        {
            Gizmos.color = Color.green;
            foreach (RectSpaceArea area in corridors)
            {
                foreach (Edge edge in area.GetEdges())
                    Gizmos.DrawLine(edge.from, edge.to);
            }
        }
    }

    private void InitMap()
    {
        for (int i = 0; i < map.GetLength(0); ++i)
        {
            for (int j = 0; j < map.GetLength(1); ++j)
                map[i, j] = CellType.Wall;
        }
    }

    private void UpdateMap(CellType[,] newMap, int minX, int minY)
    {
        for (int i = 0; i < newMap.GetLength(0); ++i)
        {
            for (int j = 0; j < newMap.GetLength(1); ++j)
            {
                map[i + minX, j + minY] = newMap[i, j];
            }
        }
    }

    private void GenerateMapMesh()
    {
        CellType[,] borderedMap = new CellType[WIDTH + borderSize * 2, HEIGHT + borderSize * 2];

        for (int i = 0; i < borderedMap.GetLength(0); ++i)
        {
            for (int j = 0; j < borderedMap.GetLength(1); ++j)
            {
                if (i >= borderSize && i < WIDTH + borderSize && j >= borderSize && j < HEIGHT + borderSize)
                {
                    borderedMap[i, j] = map[i - borderSize, j - borderSize];
                }
                else
                {
                    borderedMap[i, j] = CellType.Wall;
                }
            }
        }

        MeshGenerator meshGenerator = GetComponent<MeshGenerator>();
        meshGenerator.GenerateMesh(borderedMap, SQUARE_SIZE);
    }

    #region BSP MAP GENERATION

    private void CreateRooms()
    {
        if (bsp != null)
        {
            int room_min_x;
            int room_max_x;
            int room_min_y;
            int room_max_y;

            foreach (var leaf in bsp.GetLeaves())
            {
                room_min_x = Mathf.FloorToInt(leaf.value.minX + Random.Range(1, leaf.value.Width() / 4));
                room_min_y = Mathf.FloorToInt(leaf.value.minY + Random.Range(1, leaf.value.Height() / 4));
                room_max_x = Mathf.FloorToInt(leaf.value.maxX - Random.Range(1, leaf.value.Width() / 4));
                room_max_y = Mathf.FloorToInt(leaf.value.maxY - Random.Range(1, leaf.value.Height() / 4));

                for (int i = room_min_x; i < room_max_x; ++i)
                {
                    for (int j = room_min_y; j < room_max_y; ++j)
                    {
                        map[i, j] = CellType.BSPRoom;
                    }
                }

                rooms.Add(new RectSpaceArea(room_min_x, room_max_x, room_min_y, room_max_y));
            }
        }
    }

    private void CreateCorridor(BSP parent)
    {
        if (parent != null)
        {
            BSP start = (BSP)parent.left_child;
            BSP end = (BSP)parent.right_child;

            int start_x = Mathf.FloorToInt(start.value.minX + start.value.Width() / 2);
            int end_x = Mathf.FloorToInt(end.value.minX + end.value.Width() / 2);
            int start_y = Mathf.FloorToInt(start.value.minY + start.value.Height() / 2);
            int end_y = Mathf.FloorToInt(end.value.minY + end.value.Height() / 2);

            if (parent.value.horizontalSplit)
            {
                start_y -= 1;
                end_y += 1;
            }
            else if (parent.value.verticalSplit)
            {
                start_x -= 1;
                end_x += 1;
            }

            for (int i = start_x; i < end_x; ++i)
            {
                for (int j = start_y; j < end_y; ++j)
                    map[i, j] = map[i, j] != CellType.BSPRoom ? CellType.Corridor : CellType.BSPRoom;
            }

            corridors.Add(new RectSpaceArea(start_x, end_x, start_y, end_y));
        }
    }

    private void CreateCorridors()
    {
        foreach (var cell in bsp)
        {
            if (!cell.IsLeaf())
                CreateCorridor((BSP)cell);
        }
    }

    #endregion

    #region CELLULAR AUTOMATA MAP GENERATION

    private bool IsCorridorBorder(int row, int col)
    {
        for (int i = row - 1; i <= row + 1; ++i)
        {
            for (int j = col - 1; j <= col + 1; ++j)
            {
                if (i >= 0 && i < map.GetLength(0) && j >= 0 && j < map.GetLength(1))
                {
                    if (i != row || j != col)
                    {
                        if (map[i, j] == CellType.Corridor)
                            return true;
                    }
                }
            }
        }

        return false;
    }

    private void SetCorridorBorderCells()
    {
        for (int i = 0; i < map.GetLength(0); ++i)
        {
            for (int j = 0; j < map.GetLength(1); ++j)
            {
                if (map[i, j] == CellType.Wall && IsCorridorBorder(i, j))
                {
                    map[i, j] = CellType.CorridorBorder;
                }
            }
        }
    }

    private void InitializeArea(int minX, int maxX, int minY, int maxY)
    {
        for (int i = minX; i < maxX; ++i)
        {
            for (int j = minY; j < maxY; ++j)
            {
                if (map[i, j] == CellType.Wall)
                    map[i, j] = Random.Range(0f, 1f) <= roomFillRate ? CellType.Room : CellType.Wall;
                if (map[i, j] == CellType.CorridorBorder)
                    map[i, j] = Random.Range(0f, 1f) <= corridorFillRate ? CellType.CorridorBorderRoom : CellType.CorridorBorderWall;
            }
        }
    }

    private CellCounters CountSurroundings(int row, int col, int minX, int maxX, int minY, int maxY)
    {
        CellCounters counters = new CellCounters();

        for (int i = row - 1; i <= row + 1; ++i)
        {
            for (int j = col - 1; j <= col + 1; ++j)
            {
                if (i >= minX && i < maxX && j >= minY && j < maxY)
                {
                    if (i != row || j != col)
                    {
                        counters.roomCount += map[i, j] == CellType.Room || map[i, j] == CellType.BSPRoom ? 1 : 0;
                        counters.wallCount += map[i, j] == CellType.Wall ? 1 : 0;
                        counters.corridorBorderWallCount += map[i, j] == CellType.CorridorBorderWall ? 1 : 0;
                        counters.corridorBorderRoomCount += map[i, j] == CellType.CorridorBorderRoom ? 1 : 0;
                    }
                }
                else
                {
                    counters.wallCount += 1;
                }
            }
        }

        return counters;
    }

    private CellType[,] ApplyRules(int minX, int minY, int width, int height)
    {
        CellCounters counters;
        CellType[,] newMap = new CellType[width, height];

        for (int i = 0; i < newMap.GetLength(0); ++i)
        {
            for (int j = 0; j < newMap.GetLength(1); ++j)
            {
                switch (map[i + minX, j + minY])
                {
                    case CellType.BSPRoom:
                    case CellType.Corridor:
                        newMap[i, j] = map[i + minX, j + minY];
                        break;

                    case CellType.Wall:
                    case CellType.Room:
                        counters = CountSurroundings(i + minX, j + minY, minX, minX + width, minY, minY + height);
                        if (counters.corridorBorderRoomCount == 0)
                        {
                            if (counters.wallCount > 4)
                                newMap[i, j] = CellType.Wall;
                            else if (counters.wallCount < 4)
                                newMap[i, j] = CellType.Room;
                            else
                                newMap[i, j] = map[i + minX, j + minY];
                        }
                        else
                        {
                            if (map[i + minX, j + minY] != CellType.Room)
                                newMap[i, j] = map[i + minX, j + minY];
                            else
                                newMap[i, j] = CellType.CorridorBorderWall;
                        }
                        break;

                    case CellType.CorridorBorderWall:
                    case CellType.CorridorBorderRoom:
                        counters = CountSurroundings(i + minX, j + minY, minX, minX + width, minY, minY + height);
                        if (counters.roomCount > 0)
                            newMap[i, j] = CellType.CorridorBorderWall;
                        else
                            newMap[i, j] = CellType.CorridorBorderRoom;
                        break;

                    default:
                        return newMap;
                }
            }
        }

        return newMap;
    }

    private void ApplyAutomata(RectSpaceArea area, int numIterations)
    {
        CellType[,] newMap;
        InitializeArea(area.minX, area.maxX, area.minY, area.maxY);
        for (int iteration = 0; iteration < numIterations; ++iteration)
        {
            newMap = ApplyRules(area.minX, area.minY, area.Width(), area.Height());
            UpdateMap(newMap, area.minX, area.minY);
        }
    }
    
    #endregion

    private List<RectSpaceArea> rooms;
    private List<RectSpaceArea> corridors;

    private BSP bsp;
    private CellType[,] map;

    private const int WIDTH = 200;
    private const int HEIGHT = 200;
    private const float MIN_SPLIT_PERCENTAGE = 0.25f;
    private const float MAX_SPLIT_PERCENTAGE = 0.75f;
    private const float SQUARE_SIZE = 1f;
    private const int NUMBER_OF_ITERATIONS = 10;
}

[CustomEditor(typeof(DungeonGenerator))]
public class DungeonGeneratorEditor : Editor
{
    public override void OnInspectorGUI()
    {
        DungeonGenerator dungeonGenerator = (DungeonGenerator)target;

        dungeonGenerator.randomSeed = EditorGUILayout.IntField("Random Seed", dungeonGenerator.randomSeed);

        EditorGUILayout.Separator();

        dungeonGenerator.numberOfRooms = EditorGUILayout.IntSlider("Number of Rooms", dungeonGenerator.numberOfRooms, 20, 50);

        dungeonGenerator.drawBSP = EditorGUILayout.Toggle("Draw BSP", dungeonGenerator.drawBSP);
        dungeonGenerator.drawRooms = EditorGUILayout.Toggle("Draw Rooms", dungeonGenerator.drawRooms);
        dungeonGenerator.drawCorridors = EditorGUILayout.Toggle("Draw Corridors", dungeonGenerator.drawCorridors);

        EditorGUILayout.Separator();
        
        float room_fill_rate = EditorGUILayout.FloatField("Room Fill Rate", dungeonGenerator.roomFillRate);
        dungeonGenerator.roomFillRate = room_fill_rate > 0 && room_fill_rate < 1 ? room_fill_rate : dungeonGenerator.roomFillRate;

        float corridor_fill_rate = EditorGUILayout.FloatField("Corridor Fill Rate", dungeonGenerator.corridorFillRate);
        dungeonGenerator.corridorFillRate = corridor_fill_rate > 0 && corridor_fill_rate < 1 ? corridor_fill_rate : dungeonGenerator.corridorFillRate;

        EditorGUILayout.Separator();

        if (GUILayout.Button("Generate Dungeon"))
        {
            dungeonGenerator.GenerateDungeon();
        }
    }
}

#region SUPPORT DATA STRUCTURES

public enum CellType
{
    BSPRoom,
    Room,
    Wall,
    Corridor,
    CorridorBorder,
    CorridorBorderWall,
    CorridorBorderRoom
}

public struct CellCounters
{
    public CellCounters(int roomCount = 0, int wallCount = 0, int corridorBorderRoomCount = 0, int corridorBorderWallCount = 0)
    {
        this.roomCount = roomCount;
        this.wallCount = wallCount;
        this.corridorBorderRoomCount = corridorBorderRoomCount;
        this.corridorBorderWallCount = corridorBorderWallCount;
    }

    public int roomCount;
    public int wallCount;
    public int corridorBorderWallCount;
    public int corridorBorderRoomCount;
}

#endregion