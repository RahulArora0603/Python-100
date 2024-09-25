
#Python code that does nothing😴

def i_do_nothing():
    running = True
    while running:
        running = False

def calls_i_do_nothing():
    i_do_nothing()

def do_nothing_of_relevance():
    calls_i_do_nothing()


do_nothing_of_relevance()

