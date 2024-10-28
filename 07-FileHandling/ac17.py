with open("data.txt","r", encoding="utf-8")as file:
    lines=file.readlines()
    line_count=len(lines)
    current_line=0
    while current_line<line_count:
        for i in range(current_line, min(current_line+5, line_count)):
            print(lines[i])
        current_line+=5

        if current_line<line_count:
               input("Press Enter to display the next five lines: ")
        else:
            print("End of file reached.")
            
        break
