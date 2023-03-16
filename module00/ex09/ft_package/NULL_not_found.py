def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None", type(object))
    elif isinstance(object, float) and object != object:
        print("Cheese: nan", type(object))
    elif object is False:
        print("Fake:", object, type(object))
    elif object == 0:
        print("Zero:", object, type(object))
    elif object == '':
        print("Empty:", type(object))
    else:
        print("Type not Found")
        return 1

    return 0

# if __name__ == "__main__":
#
#     Nothing = None
#     Garlic = float("NaN")
#     Zero = 0
#     Empty = ''
#     Fake = False
#     NULL_not_found(Nothing)
#     NULL_not_found(Garlic)
#     NULL_not_found(Zero)
#     NULL_not_found(Empty)
#     NULL_not_found(Fake)
#     print(NULL_not_found("Brian"))
