def list_to_string_without_commas(pList) :
    string  =   ""
    for element in pList :
        string = string + element
    
    return string

def test() :
    print("\n")
    print("Lets try to convert this List in a String:")
    print(" - ['Alfa', 'Beta', 'Gama']")
    print("\n")

    lista = ['Alfa', 'Beta', 'Gama']
    string = list_to_string_without_commas(lista)

    print("The String result is:")
    print(string)

if ( __name__ == "__main__" ) :
    test()
