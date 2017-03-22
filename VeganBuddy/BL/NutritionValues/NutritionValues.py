class NutritionValues(object):
    """
    This class represents the NutritionValues story.
    """
    def __init__(self):
        pass

    @staticmethod
    def get_nutrition_value(context, entities):
        print "Yay"
        context['nutrition_value'] = '42'
        return context
