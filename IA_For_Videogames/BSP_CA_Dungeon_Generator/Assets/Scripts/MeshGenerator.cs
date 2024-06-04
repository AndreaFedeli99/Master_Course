using System.Collections.Generic;
using UnityEngine;

public class MeshGenerator : MonoBehaviour
{
    public SquareGrid squareGrid;
    private List<Vector3> vertices;
    private List<int> indexes;

    public void GenerateMesh(CellType[,] map, float squareSize)
    {
        squareGrid = new SquareGrid(map, squareSize);

        vertices = new List<Vector3>();
        indexes = new List<int>();

        for (int i = 0; i < squareGrid.squares.GetLength(0); ++i)
        {
            for (int j = 0; j < squareGrid.squares.GetLength(1); ++j)
            {
                TriangulateSquare(squareGrid.squares[i, j]);
            }
        }

        Mesh mesh = new Mesh();
        GetComponent<MeshFilter>().mesh = mesh;

        mesh.vertices = vertices.ToArray();
        mesh.triangles = indexes.ToArray();
        mesh.RecalculateNormals();
    }

    private void TriangulateSquare(Square square)
    {
        switch (square.configuration)
        {
            // 1 control node enabled:
            case 1:
                CreateMeshFromPoints(square.bottom, square.bottomLeft, square.left);
                break;
            case 2:
                CreateMeshFromPoints(square.right, square.bottomRight, square.bottom);
                break;
            case 4:
                CreateMeshFromPoints(square.top, square.topRight, square.right);
                break;
            case 8:
                CreateMeshFromPoints(square.topLeft, square.top, square.left);
                break;

            // 2 control nodes enabled:
            case 3:
                CreateMeshFromPoints(square.right, square.bottomRight, square.bottomLeft, square.left);
                break;
            case 6:
                CreateMeshFromPoints(square.top, square.topRight, square.bottomRight, square.bottom);
                break;
            case 9:
                CreateMeshFromPoints(square.topLeft, square.top, square.bottom, square.bottomLeft);
                break;
            case 12:
                CreateMeshFromPoints(square.topLeft, square.topRight, square.right, square.left);
                break;
            case 5:
                CreateMeshFromPoints(square.top, square.topRight, square.right, square.bottom, square.bottomLeft, square.left);
                break;
            case 10:
                CreateMeshFromPoints(square.topLeft, square.top, square.right, square.bottomRight, square.bottom, square.left);
                break;

            // 3 control nodes enabled:
            case 7:
                CreateMeshFromPoints(square.top, square.topRight, square.bottomRight, square.bottomLeft, square.left);
                break;
            case 11:
                CreateMeshFromPoints(square.topLeft, square.top, square.right, square.bottomRight, square.bottomLeft);
                break;
            case 13:
                CreateMeshFromPoints(square.topLeft, square.topRight, square.right, square.bottom, square.bottomLeft);
                break;
            case 14:
                CreateMeshFromPoints(square.topLeft, square.topRight, square.bottomRight, square.bottom, square.left);
                break;

            // 4 control nodes enabled:
            case 15:
                CreateMeshFromPoints(square.topLeft, square.topRight, square.bottomRight, square.bottomLeft);
                break;
        }
    }

    private void CreateMeshFromPoints(params SimpleNode[] points)
    {
        AddVertices(points);
        CreateTriangles(points);
    }

    private void AddVertices(SimpleNode[] points)
    {
        foreach (SimpleNode point in points)
        {
            if (point.vertexIndex == -1)
            {
                point.vertexIndex = vertices.Count;
                vertices.Add(point.position);
            }
        }
    }

    private void CreateTriangles(SimpleNode[] points)
    {
        SimpleNode mainVertex = points[0];
        int vertexShift = 1;
        while (vertexShift < points.Length - 1)
        {
            this.indexes.Add(mainVertex.vertexIndex);

            for (int i = vertexShift; i <= vertexShift + 1; ++i)
            {
                this.indexes.Add(points[i].vertexIndex);
            }

            vertexShift++;
        }
    }

    private void Start()
    {
        GetComponent<MeshFilter>().mesh = null;
    }

    public class SquareGrid
    {
        public Square[,] squares;
        
        public SquareGrid(CellType[,] map, float squareSize)
        {
            float mapWidth = map.GetLength(0) * squareSize;
            float mapHeight = map.GetLength(1) * squareSize;

            ControlNode[,] controlNodes = new ControlNode[map.GetLength(0), map.GetLength(1)];

            for (int i = 0; i < controlNodes.GetLength(0); ++i)
            {
                for (int j = 0; j < controlNodes.GetLength(1); ++j)
                {
                    Vector3 position = new Vector3(-mapWidth / 2 + i * squareSize + squareSize / 2, 0, -mapHeight / 2 + j * squareSize + squareSize / 2);
                    controlNodes[i, j] = new ControlNode(position, DungeonGenerator.IsCellActive(map[i, j]), squareSize); ;
                }
            }

            squares = new Square[map.GetLength(0) - 1, map.GetLength(1) - 1];

            for (int i = 0; i < squares.GetLength(0); ++i)
            {
                for (int j = 0; j < squares.GetLength(1); ++j)
                {
                    squares[i, j] = new Square(controlNodes[i, j + 1], controlNodes[i + 1, j + 1], controlNodes[i + 1, j], controlNodes[i, j]);
                }
            }
        }
    }

    public class Square
    {
        public ControlNode topLeft, topRight, bottomRight, bottomLeft;
        public SimpleNode top, right, bottom, left;
        public int configuration;

        public Square(ControlNode topLeft, ControlNode topRight, ControlNode bottomRight, ControlNode bottomLeft)
        {
            this.topLeft = topLeft;
            this.topRight = topRight;
            this.bottomRight = bottomRight;
            this.bottomLeft = bottomLeft;

            this.top = topLeft.right;
            this.right = bottomRight.above;
            this.bottom = bottomLeft.right;
            this.left = bottomLeft.above;

            if (topLeft.active)
                configuration += 8;
            if (topRight.active)
                configuration += 4;
            if (bottomRight.active)
                configuration += 2;
            if (bottomLeft.active)
                configuration += 1;
        }
    }

    public class SimpleNode
    {
        public Vector3 position;
        public int vertexIndex = -1;

        public SimpleNode(Vector3 pos)
        {
            this.position = pos;
        }
    }

    public class ControlNode : SimpleNode
    {
        public bool active;
        public SimpleNode right, above;

        public ControlNode(Vector3 pos, bool active, float squareSize) : base(pos)
        {
            this.active = active;
            above = new SimpleNode(pos + Vector3.forward * squareSize / 2f);
            right = new SimpleNode(pos + Vector3.right * squareSize / 2f);
        }
    }
}
