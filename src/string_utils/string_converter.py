"""String utility functions"""

def path_to_str(path: list[int]) -> str:
	"""
	Convert array of paths to str for storage in network database\n
	Example:\n
	`path_to_str([12, 4, 55, 67])`\n
	Returns: `"12 -> 4 -> 55 -> 67"
	"""
	return " -> ".join(map(str, path))

def str_path_to_list(path_str: str) -> list[int]:
	"""
	Convert network database path string to an array of paths\n
	Example:\n
	`str_path_to_list("12 -> 4 -> 55 -> 67")`\n
	Returns: `[12, 4, 55, 67]`
	"""
	return map(int, path_str.split(" -> "))