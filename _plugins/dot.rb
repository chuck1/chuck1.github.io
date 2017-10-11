
module Jekyll
	class DotConverter < Converter
		safe true
		priority :low

		def matches(ext)
			ext =~ /^\.dot$/i
		end

		def output_ext(ext)
			".svg"
		end

		def convert(content)
			file = "/home/crymal/temp1"
			open(file, 'w') { |f|
				f.puts "#{content}"
			}
			
			#puts "dot"
			#puts content
			
			`dot -Tsvg #{file}`
		end
	end
	class NeatoConverter < Converter
		safe true
		priority :low

		def matches(ext)
			ext =~ /^\.neato$/i
		end

		def output_ext(ext)
			".svg"
		end

		def convert(content)
			file = "/home/crymal/temp1"
			#file = `mktemp`

			#puts "neato"
			#puts file
			#puts content

			open(file, 'w') { |f|
				f.puts "#{content}"
			}

			`neato -Tsvg #{file}`
		end
	end
	class PyplotConverter < Converter
		safe true
		priority :low

		def matches(ext)
			ext =~ /^\.py$/i
		end

		def output_ext(ext)
			".svg"
		end

		def convert(content)
			file = "/home/crymal/temp1"

			#puts "pyplot"
			#puts file
			#puts content

			open(file, 'w') { |f|
				f.puts "#{content}"
			}

			`python3 #{file}`
		end
	end
end

