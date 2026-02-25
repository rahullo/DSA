
def simplifyPath(path):
    stack = []
    
    # Split by '/' results in parts like ["home", "", "foo", ".."]
    parts = path.split("/")
    print("Parts: ", parts)
    for part in parts:
        if part == "..":
            # Go up one level if possible
            if stack:
                print("Popping: ", stack[-1])
                stack.pop()
        elif part == "." or not part:
            # Ignore current directory or empty strings from '//'
            continue
        else:
            # It's a valid directory name (like "home" or "...")
            stack.append(part)
    
    # Join with '/' and ensure leading slash
    return "/" + "/".join(stack)

print(simplifyPath("/home///user/Documents//../Pictures"))