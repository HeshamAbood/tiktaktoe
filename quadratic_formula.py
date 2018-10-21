import logging
import math

#create and configure logger
LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "D:\\old\\e\\learn\\Python\\Learn_h\\lumberjack.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger=logging.getLogger()

def quadratic_formula(a,b,c):
    """Return the solution to the equation ax^2 + bx + c =0. """
    logger.info("quadratic_formula({0}, {1}, {2})".format(a,b,c))
    disc= b**2 - 4*a*c

    # Compute the discriminant
    logger.debug(" # Compute the discriminant")
    root1=(-b + math.sqrt(disc))/(2*a)
    root2=(-b - math.sqrt(disc))/(2*a)

    # Return the roots
    logger.debug("# Return the roots")
    return (root1, root2)

roots = quadratic_formula(1,0,1)
print(roots)


