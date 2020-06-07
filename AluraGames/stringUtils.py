def list_to_string_without_commas(pList) :
    string  =   ""
    for element in pList :
        string = string + str(element)
    
    return string

def list_to_string_with_commas(pList) :
    string  =   ""
    comma   =   ""
    for element in pList :
        string = string + comma + str(element)
        comma = ", "
    
    return string

def string_to_list(pString) :
    lista = ["_"] * len( pString )

    index = 0
    for char in pString :
        lista[index]    =   char
        index = index + 1
    
    return lista

def test_list_to_string_without_commas() :
    print("\n")
    print("Lets try to convert this List in a String:")
    print(" - ['Alfa', 'Beta', 'Gama']")
    print("\n")

    lista = ['Alfa', 'Beta', 'Gama']
    string = list_to_string_without_commas(lista)

    print("The String result is:")
    print(string)

def test_list_to_string_with_commas() :
    print("\n")
    print("Lets try to convert this List in a String:")
    print(" - ['Alfa', 'Beta', 'Gama']")
    print("\n")

    lista = ['Alfa', 'Beta', 'Gama']
    string = list_to_string_with_commas(lista)

    print("The String result is:")
    print(string)

def test_string_to_list() :
    string = "banana"
    lista = string_to_list(string)

    print("\n")
    print("Lets try to convert this String in a List:")
    print(" - 'banana'")
    print("\n")

    print(lista)

if ( __name__ == "__main__" ) :
    test_list_to_string_with_commas()
