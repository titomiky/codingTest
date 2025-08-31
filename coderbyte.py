def TreeConstructor(strArr):
    # Return "false" for empty input
    if not strArr:
        return "false"
    # Map each child to its parent
    child_parent = {}
    # Count how many children each parent has
    parent_children = {}
    # Process every "(child,parent)" string
    for raw in strArr:
        # Ensure the string uses parentheses correctly
        if not raw.startswith("(") or not raw.endswith(")"):
            return "false"
        # Attempt to split into child and parent numbers
        try:
            child_str, parent_str = raw[1:-1].split(",")
            child = int(child_str.strip())
            parent = int(parent_str.strip())
        except Exception:
            return "false"
        # Each child must have only one parent
        if child in child_parent and child_parent[child] != parent:
            return "false"
        # Record the parent of the child
        child_parent[child] = parent
        # Increment the parent's child count
        parent_children[parent] = parent_children.get(parent, 0) + 1
        # A parent cannot have more than two children
        if parent_children[parent] > 2:
            return "false"
    # Gather every node seen in the pairs
    all_nodes = set(child_parent) | set(parent_children)
    # Identify roots: parents that never appear as children
    roots = set(parent_children) - set(child_parent)
    # There must be exactly one root
    if len(roots) != 1:
        return "false"
    # Verify the edge count equals node count minus one
    if len(child_parent) != len(all_nodes) - 1:
        return "false"
    # All rules passed: valid binary tree
    return "true"

print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"])) 
print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]))        # ➞ "true"
print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,1)", "(1,4)"])) # ➞ "false"
