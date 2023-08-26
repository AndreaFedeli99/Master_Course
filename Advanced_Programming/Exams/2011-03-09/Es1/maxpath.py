def maxpath(levels):
    if not levels:
        return 0

    def maxpath_recursive(level_idx, node_idx):
        if level_idx < 0 or node_idx < 0 or node_idx >= len(levels[level_idx]):
            return 0
        current_node = levels[level_idx][node_idx]
        left_path = maxpath_recursive(level_idx - 1, node_idx - 1)
        right_path = maxpath_recursive(level_idx - 1, node_idx)
        return current_node + max(left_path, right_path)

    last_level = levels[-1]
    return max([maxpath_recursive(len(levels) - 1, i) for i in range(len(last_level))])
