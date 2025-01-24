def welcome_massage(tittle) :
    style = '*' * (len(tittle) + 8)
    print(style)
    print(f'**  {tittle}  **')
    print(f'{style}\n')
    print()
    
if __name__ == '__main__' :
    welcome_massage()