#!/usr/bin/env ruby
log = ARGV[0]

matches = log.scan(/\[from:(\+\d+)\] \[to:(\+\d+)\] \[flags:(.*?)\]/)
matches.each do |match|
  sender = match[0]
  receiver = match[1]
  flags = match[2]
  puts "#{sender},#{receiver},#{flags}"
end
