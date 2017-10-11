
module Jekyll
	class Map < Jekyll::Generator
		safe true
		priority :lowest

		def generate(site)
			puts site
			#puts site.pages
			site.pages.each do |page|
				puts page.dir
				puts page.name
			end
		end
	end
end

