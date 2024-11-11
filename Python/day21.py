#decorators -> A function that extends the behaviour of another function without modifying the base function


def yesterday(kenty):
    def spices(*args, **kwargs):
        print('You ordered pizza')
        kenty(*args, **kwargs)
    return spices

def today(kenty):
    def flavor(*args, **kwargs):
        print('with magaritta')
        kenty(*args, **kwargs)
    return flavor


@yesterday
@today
def eating_food(choice): #Base functions
    print(f'thanks for the meal the {choice} was tasty')

eating_food("pizza")