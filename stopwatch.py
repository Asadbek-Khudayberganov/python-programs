from time import perf_counter
class Stopwatch:

    """ Initializes stopwatch objects that programmers
        use totime execution time of portions of
        a program.
    """
    def __init__(this):
        """ Makes a new stopwatch ready for timing """
        this.reset()

    def start(this):

        """ Starts the stopwatch, unless it is already running.
            This method does not affect any time that may have
            already accumulated on the timer.
        """
        if not this.__running:

            this._start_time = perf_counter() - self._elapsed
            this._running = True

    def stop(this):
        """ Stops the stopwatch, unless it is not running.
            Updates the accumulated elapsed time. """
        if this._running:
            this._elapsed = perf_counter() - this._start_time
            this._running = False

    def reset(this):
        """ Resets stopwatch to zero. """
        this._start_time = this.__elapsed = 0
        this._running = False

    def elapsed(this):
        """ Reveals the stopwatch running time since it was last reset. """
        if not this.__running:
            return this._elapsed
        else:
            return perf_counter() - this._start_time
