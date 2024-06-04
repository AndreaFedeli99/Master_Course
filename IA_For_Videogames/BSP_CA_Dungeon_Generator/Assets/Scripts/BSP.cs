using System.Collections.Generic;
using UnityEngine;

public class BSP : TreeNode<RectSpaceArea>
{
    #region CONSTRUCTORS

    public BSP(RectSpaceArea nodeValue) : base(nodeValue) { }

    public BSP(RectSpaceArea nodeValue, BSP left, BSP right) : base(nodeValue, left, right) { }

    #endregion

    #region PUBLIC METHODS

    public void BuildBSP(int numSplit, float min_split, float max_split)
    {
        BSP current = this;
        List<BSP> areasToSplit = new List<BSP>();

        this.MinSplit = min_split;
        this.MaxSplit = max_split;

        for (int i = 0; i < numSplit; i++)
        {
            MakeSplit(current);

            areasToSplit.Add((BSP)current.left_child);
            areasToSplit.Add((BSP)current.right_child);

            int index = GetNextAreaToSplit(areasToSplit);
            current = areasToSplit[index];
            areasToSplit.RemoveAt(index);
        }
    }

    public void DrawBSP()
    {
        this.DrawNode(this);
    }

    #endregion

    #region SETTERS/GETTERS

    public float MinSplit
    {
        get { return min_split; }
        private set
        {
            if (value < max_split && value >= 0.15f && value <= 0.85f)
                this.min_split = value;
            else
                this.min_split = 0.25f;
        }
    }
    public float MaxSplit
    {
        get { return this.max_split; }
        private set
        {
            if (value > min_split && value >= 0.15f && value <= 0.85f)
                this.max_split = value;
            else
                this.max_split = 0.75f;
        }
    }
    
    #endregion

    private float min_split;
    private float max_split;
    private const float H_RATIO = 0.45f;
    private const float W_RATIO = 0.45f;

    #region PRIVATE METHODS

    private void MakeSplit(BSP node)
    {
        // Horizontal split
        if (Random.Range(0, 2) == 0)
        {
            HorizontalSplit(node);
        }
        // Vertical split
        else
        {
            VerticalSplit(node);
        }
    }

    private void VerticalSplit(BSP node)
    {
        int split = Mathf.FloorToInt(Mathf.Lerp(node.value.minY, node.value.maxY, Random.Range(this.MinSplit, this.MaxSplit)));
        RectSpaceArea left_area = new RectSpaceArea(node.value.minX, node.value.maxX, node.value.minY, split);
        RectSpaceArea right_area = new RectSpaceArea(node.value.minX, node.value.maxX, split, node.value.maxY);
        if (((float)left_area.Height() / left_area.Width()) < H_RATIO || ((float)right_area.Height() / right_area.Width()) < H_RATIO)
        {
            MakeSplit(node);
            return;
        }

        BSP left = new BSP(left_area);
        BSP right = new BSP(right_area);

        node.left_child = left;
        node.right_child = right;
        node.value.verticalSplit = true;
    }

    private void HorizontalSplit(BSP node)
    {
        int split = Mathf.FloorToInt(Mathf.Lerp(node.value.minX, node.value.maxX, Random.Range(this.MinSplit, this.MaxSplit)));
        RectSpaceArea left_area = new RectSpaceArea(node.value.minX, split, node.value.minY, node.value.maxY);
        RectSpaceArea right_area = new RectSpaceArea(split, node.value.maxX, node.value.minY, node.value.maxY);
        if (((float)left_area.Width() / left_area.Height()) < W_RATIO || ((float)right_area.Width() / right_area.Height()) < W_RATIO)
        {
            MakeSplit(node);
            return;
        }

        BSP left = new BSP(left_area);
        BSP right = new BSP(right_area);

        node.left_child = left;
        node.right_child = right;
        node.value.horizontalSplit = true;
    }

    private int GetNextAreaToSplit(List<BSP> areas)
    {
        int maxArea = areas[0].value.Area();
        int selectedElement = 0;
        for (int i = 0; i < areas.Count; i++)
        {
            if (maxArea < areas[i].value.Area())
            {
                maxArea = areas[i].value.Area();
                selectedElement = i;
            }
        }
        return selectedElement;
    }

    private void DrawNode(BSP current)
    {
        if (current.IsLeaf())
        {
            foreach (Edge edge in current.value.GetEdges())
            {
                Gizmos.DrawLine(edge.from,edge.to);
            }
            return;
        }

        DrawNode((BSP)current.left_child);
        DrawNode((BSP)current.right_child);
    }
    
    #endregion
}
