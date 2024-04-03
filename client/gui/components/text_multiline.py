from .text_oneline import text_oneline
import pygame

class text_multiline(text_oneline):

	def update_text(self, text):
		self.rendered_surface = pygame.Surface(self.size)
		texts = []
		for line in text.split("\n"):
			texts.append(self.font.render(line, True, self.color))

		height_per_text = self.size[1]/len(texts)

		max_height_factor = min([1/(text_surface.get_height()/height_per_text) for text_surface in texts])
		max_width_factor = min([1/(text_surface.get_width()/self.size[0]) for text_surface in texts])
		factor = min(max_width_factor, max_height_factor)
		for text_surface in texts:
			scaled_text_surface = pygame.transform.scale_by(text_surface, factor)
			self.rendered_surface.blit(scaled_text_surface, (0, scaled_text_surface.get_height() * texts.index(text_surface)))

	def render_on(self, surface):
		pygame.draw.rect(surface, self.border_color, self.border)
		pygame.draw.rect(surface, self.filler_color, self.position + self.size)
		surface.blit(self.rendered_surface, self.position) #I dont think it is worth centering
