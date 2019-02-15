def color_addition(c1:str, c2:str) -> str:
    if c1 == c2:
       return c1
    return 'RGB'.replace(c1,'').replace(c2,'')



def triangle(row:str) -> str:
    row = list(row)
    space = 1
    while len(row) != 1:
        print(' ' * space, *row)
        row = [ color_addition(row[i],row[i+1]) for i in range(len(row)-1) ]
        space += 1
    print(' ' * space, *row)
    return row[0]



def main():
    row = list('RRGBRGBB')
    triangle(row)



if __name__ == "__main__":
    main()