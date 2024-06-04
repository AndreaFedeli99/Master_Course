using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class TreeNode<NodeValue> : IEnumerable<TreeNode<NodeValue>>
{
    #region CONSTRUCTORS

    /// <summary>
    /// Construct a TreeNode with the specified value
    /// </summary>
    /// <param name="value">Value of the node</param>
    public TreeNode(NodeValue value) { this.value = value; }
    /// <summary>
    /// Construct a TreeNode with the specified value and left/right children
    /// </summary>
    /// <param name="value">Value of the node</param>
    /// <param name="left">Reference to the left child</param>
    /// <param name="right">Refernce to the right child</param>
    public TreeNode(NodeValue value, TreeNode<NodeValue> left, TreeNode<NodeValue> right) : this(value)
    {
        this.left_child = left;
        this.right_child = right;
    }
    
    #endregion

    public NodeValue value { get; private set; }
    public TreeNode<NodeValue> left_child { get; set; }
    public TreeNode<NodeValue> right_child { get; set; }

    #region PUBLIC METHODS

    public bool IsLeaf() { return left_child == null && right_child == null; }

    public TreeNode<NodeValue>[] GetLeaves()
    {
        if (IsLeaf())
            return new TreeNode<NodeValue>[] { this };
        else
            return new List<TreeNode<NodeValue>>().Concat(left_child.GetLeaves()).Concat(right_child.GetLeaves()).ToArray();
    }

    public TreeNode<NodeValue>[] GetChildrenAtLevel(int level, List<TreeNode<NodeValue>> nodes = null)
    {
        if (nodes == null)
            nodes = new List<TreeNode<NodeValue>>();
        if (level == 1)
        {
            nodes.Add(this);
        }
        else if (!IsLeaf())
        {
            left_child.GetChildrenAtLevel(level - 1, nodes);
            right_child.GetChildrenAtLevel(level - 1, nodes);
        }
        return nodes.ToArray();
    }

    public int GetHeight()
    {
        if (this.IsLeaf())
            return 1;
        return 1 + Math.Max(left_child.GetHeight(), right_child.GetHeight());
    }

    public override string ToString()
    {
        return value.ToString();
    }

    public IEnumerator<TreeNode<NodeValue>> GetEnumerator()
    {
        if (this != null)
        {
            yield return this;
            if (!this.IsLeaf())
            {
                foreach (var tree in this.left_child)
                    yield return tree;
                foreach (var tree in this.right_child)
                    yield return tree;
            }
        }
        yield break;
    }

    #endregion

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }
}
