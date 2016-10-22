from functools import wraps
from time import time, sleep
import copy

_StatsTemplate = {
	'min': None,
	'max': None,
	'avg': None,
	'total_calls': 0,
	'total_time': 0,
	'func_name': None,
	'func_uid': None
}

_RuntimeStats = {}

def runtime_stats():
	def decorating_function(user_function):
		@wraps(user_function)
		def wrapper(*args,**kwargs):
			ts = time()
			result = user_function(*args, **kwargs)
			te = time()
			elapsed_time = round((te-ts)*1000,3)
			func_uid = id(user_function)
			func_name = user_function.__name__
			rs = _RuntimeStats.get(func_uid, None)
			if not rs:
				_RuntimeStats[func_uid] = copy.copy(_StatsTemplate)
				_RuntimeStats[func_uid]['func_name'] = func_name
				_RuntimeStats[func_uid]['func_uid'] = func_uid
				rs = _RuntimeStats.get(func_uid)
			rs['total_calls'] += 1
			if (rs['min'] and elapsed_time < rs['min']) or rs['min'] is None:
				rs['min'] = elapsed_time
			
			if (rs['max'] and elapsed_time > rs['max']) or rs['max'] is None:
				rs['max'] = elapsed_time

			if (rs['avg'] and elapsed_time != rs['avg']) or rs['avg'] is None:
				rs['avg'] = (((rs['avg'] or 0)*(rs['total_calls']-1)) + elapsed_time)/rs['total_calls']
			rs['total_time'] += elapsed_time
			return result

		def get_func_runtime_stats():
			return _RuntimeStats[id(user_function)]

		def get_all_runtime_stats():
			return _RuntimeStats
		wrapper.__wrapped__ = user_function
		wrapper.get_func_runtime_stats = get_func_runtime_stats
		wrapper.get_all_runtime_stats = get_all_runtime_stats
		return wrapper
	return decorating_function