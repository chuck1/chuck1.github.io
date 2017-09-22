module Jekyll
	class CiteTag < Liquid::Tag
		def initialize(tag_name, text, tokens)
			super
			@text = text
		end
		def render(context)
			"<a href=\"/pages/literature/articles/#{@text}\">#{(@text.strip)[-4,4]}</a>"
		end
	end
end

Liquid::Template.register_tag('cite', Jekyll::CiteTag)

