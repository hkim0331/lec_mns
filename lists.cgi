#!/usr/bin/env ruby
# -*- mode: ruby; coding: utf-8 -*-

require 'cgi'
require 'sequel'

def stars(s)
  s.gsub(/[a-zA-Z0-9]/,"*")
end

DB = Sequel.sqlite("./lists.db")[:lists]

cgi = CGI.new("html5")
puts "content-type: text/html; chareset=utf-8"
puts

print <<EOH
<head>
<meta charset='utf-8'>
<title>maillist</title>
<style>
body {
font-family: sans-serif;
}

h1,h2,h3,h4 {
color: green;
}

div {
margin-left: 2em;
}

table.tabular {
border-collapse: collapse;
}

table.tabular th td {
border: 1pt solid gray;
}

.warn {
color: red;
}
</style>
</head>
EOH

begin
  if cgi.request_method == "GET"
    print <<EOT
<h2>一覧</h2>
<div>
<table class='tabular'>
<tr><th>研究室<th>代表氏名(学生)<th>email</tr>
EOT
    DB.each do |u|
      print <<EOU
<tr><td>#{u[:labo]}<td>#{u[:name]}<td>#{stars(u[:email])}</tr>
EOU
    end
    puts "</table></div>"

    print <<EOF
<h2>登録</h2>
<div>
<form method="post">
<table>
<tr><th>研究室<td><input name='labo'></tr>
<tr><th>代表氏名<td><input name='name'></tr>
<tr><th>email<td><input name='email'></tr>
<tr><th><td><input type='submit'>
</table>
</form>
</div>
EOF

  elsif cgi.request_method == "POST"
    puts "<h2>登録完了</h2>"
    DB.insert(labo: cgi['labo'], name: cgi['name'], email: cgi['email'])

    print <<EOM
<p>inserted.</p>
<p><a href="./lists.cgi">戻る</a></p>
EOM

  else
    raise "unknown method: #{cgi.request_method}"
  end

rescue => ex
  puts "<p class='warn'>#{ex.message}</p>"

ensure
  print <<EOF
<hr>
programmed by hkimura.
EOF
end

