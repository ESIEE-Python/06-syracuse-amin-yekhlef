"""
 This programme is used for syracuse lists :) !
"""

#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
       Function used to plot a syracuse list
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    u = n
    l = []
    l.append(u)

    while u != 1:
        if u % 2 == 0:
            u = u // 2
        else:
            u = (u * 3) + 1
        l.append(u)

    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    return len(l)

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici
    #print("l[0] found is : ", l[0])
    #print("n found is : ", n)
    tva = 0
    for i,e in enumerate(l):
        if e < l[0]:
            tva = i
            break
    return tva


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    return max(l)


#### Fonction principale


def main():
    """
       Main function of the programm
    """
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(4)
    #syr_plot(lsyr)
    print("tv : ", temps_de_vol(lsyr))
    print("tva : ", temps_de_vol_en_altitude(lsyr))
    print("am : ", altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
