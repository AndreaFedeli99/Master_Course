using System.Collections.Generic;
using UnityEngine;

public class RectSpaceArea
{
    #region CONSTRUCTORS

    /// <summary>
    /// Construct a SpaceArea with the specified dimensions.
    /// </summary>
    /// <param name="minX">Min x value</param>
    /// <param name="maxX">Max x value</param>
    /// <param name="minY">Min y value</param>
    /// <param name="maxY">Max y value</param>
    public RectSpaceArea(int minX, int maxX, int minY, int maxY)
    {
        this.minX = minX; this.minY = minY;
        this.maxX = maxX; this.maxY = maxY;
        this.horizontalSplit = false;
        this.verticalSplit = false;
    }

    #endregion

    public int minX { get; private set; }
    public int minY { get; private set; }
    public int maxX { get; private set; }
    public int maxY { get; private set; }
    public bool horizontalSplit { get; set; }
    public bool verticalSplit { get; set; }

    #region PUBLIC METHODS

    public Edge[] GetEdges()
    {
        List<Edge> edges = new List<Edge>
        {
            new Edge(new Vector3(minX, 0, minY), new Vector3(maxX, 0, minY)),
            new Edge(new Vector3(minX, 0, minY), new Vector3(minX, 0, maxY)),
            new Edge(new Vector3(minX, 0, maxY), new Vector3(maxX, 0, maxY)),
            new Edge(new Vector3(maxX, 0, minY), new Vector3(maxX, 0, maxY))
        };

        return edges.ToArray();
    }

    public int Area()
    {
        return this.Width() * this.Height();
    }

    public int Width()
    {
        return Mathf.Abs(maxX - minX);
    }

    public int Height()
    {
        return Mathf.Abs(maxY - minY);
    }

    public override string ToString()
    {
        return string.Format("MinX: {0:N2}\tMaxX: {1:N2}\tMinY: {2:N2}\tMaxY: {3:N2}\n", minX, maxX, minY, maxY);
    }
    
    #endregion
}

#region SUPPORT DATA STRUCTURES

public struct Edge
{
    public Edge(Vector3 from, Vector3 to)
    {
        this.from = from; this.to = to;
    }
    public Vector3 from;
    public Vector3 to;
}

#endregion
