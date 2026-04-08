# 4️⃣ Joke Teller	              pyjokes	        Get random programming jokes

import pyjokes

def tell_joke():
    '''Returns a random programming joke.'''

    joke = pyjokes.get_joke()

    print(joke)

tell_joke()