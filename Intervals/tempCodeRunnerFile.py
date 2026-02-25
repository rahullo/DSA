return 0
    
    # Step 1: Sort by the end coordinate
    # Sorting by the end ensures we are always checking 
    # the earliest possible "deadline" for a balloon.
    points.sort(key=lambda x: x[1])
    
    arrows = 1
    # Place the first arrow at the end of the first balloon
    current_arrow_pos = points[0][1]
    
    for i in range(1, len(points)):
        # If the current balloon starts after the last arrow position
        if points[i][0] > current_arrow_pos:
            # We need a new arrow
            arrows += 1
            # Place it at the end of the current balloon
            current_arrow_pos = points[i][1]
            
    return arrows