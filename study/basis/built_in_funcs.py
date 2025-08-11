def check_callable(callable_obj):
    """
    Check if the object is callable.
    
    :param callable_obj: The object to check.
    :return: True if the object is callable, False otherwise.
    """
    return callable(callable_obj)

def check_iterable(iterable_obj):
    """
    Check if the object is iterable.
    
    :param iterable_obj: The object to check.
    :return: True if the object is iterable, False otherwise.
    """
    try:
        iter(iterable_obj)
        return True
    except TypeError:
        return False

def check_instance(obj, cls):
    """
    Check if the object is an instance of the given class.
    
    :param obj: The object to check.
    :param cls: The class to check against.
    :return: True if the object is an instance of the class, False otherwise.
    """
    return isinstance(obj, cls)

def check_subclass(subclass, cls):
    """
    Check if the subclass is a subclass of the given class.
    
    :param subclass: The subclass to check.
    :param cls: The class to check against.
    :return: True if the subclass is a subclass of the class, False otherwise.
    """
    return issubclass(subclass, cls)

def sort_list(lst, reverse=False):
    """
    Sort a list in ascending or descending order.
    
    :param lst: The list to sort.
    :param reverse: If True, sort in descending order; otherwise, sort in ascending order.
    :return: The sorted list.
    """
    return sorted(lst, reverse=reverse)

def filter_list(lst, func):
    """
    Filter a list using a function.
    
    :param lst: The list to filter.
    :param func: The function to use for filtering.
    :return: A new list containing elements that satisfy the function.
    """
    return [item for item in lst if func(item)]

def map_list(lst, func):
    """
    Apply a function to each element in a list.
    
    :param
    lst: The list to map.
    :param func: The function to apply to each element.
    :return: A new list containing the results of applying the function.
    """
    return [list(map(func, lst))]

