class Shortcode():

	def __init__(self, Unprompted):
		self.Unprompted = Unprompted
		self.description = "Use within [switch] to run different logic blocks depending on the value of a var."

	def preprocess_block(self, pargs, kwargs, context):
		return True

	def run_block(self, pargs, kwargs, context, content):
		import lib_unprompted.helpers as helpers

		_var = self.Unprompted.shortcode_objects["switch"].switch_var

		# Default case
		if len(pargs) == 0:
			if _var != "":
				return (self.Unprompted.process_string(content, context))
		# Supports matching against multiple pargs
		for parg in pargs:
			if helpers.is_equal(_var, self.Unprompted.parse_advanced(parg, context)):
				self.Unprompted.shortcode_objects["switch"].switch_var = ""
				return (self.Unprompted.process_string(content, context))

		return ("")

	def ui(self, gr):
		return [
		    gr.Textbox(label="Matching value 🡢 arg_str", max_lines=1),
		]
