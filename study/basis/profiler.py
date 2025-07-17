from ncmv import default_logging
import logging
import cProfile
import pstats

def profile(func):
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        res = func(*args, **kwargs)
        profiler.disable()
        
        stats = pstats.Stats(profiler)
        stats.sort_stats('cumulative')  # Sort by cumulative time
        stats.print_stats()
    
    return wrapper

# Example usage
if __name__ == "__main__":
    @profile
    def example_function():
        total = 0
        for i in range(10000000):
            total += i
        return total

    example_function()
    logging.info("Profiler has been executed.")