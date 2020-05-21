import math

def circle( radius ):
    return round( math.pi * ( radius**2 ), 2)

def triangle( base, height ):
    return  ( base * height )/2

def rectangle( base, height ):
    return base * height

def donut( outside_radius, inside_radius ):
    return round( circle( outside_radius ) - circle( inside_radius ), 2 )

print( circle    ( 3 ) )
print( triangle  ( 5, 5 ) )
print( rectangle ( 8, 8 ) )
print( donut     ( 10, 8 ) )