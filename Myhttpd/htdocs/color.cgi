#!/usr/bin/perl
#

local ($buffer, @pairs, $pair, $name, $value, %FORM);

$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;
if ($ENV{'REQUEST_METHOD'} eq "POST")
{
   read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
}else {
   $buffer = $ENV{'QUERY_STRING'};
}

@pairs = split(/&/, $buffer);
foreach $pair (@pairs)
{
   ($name, $value) = split(/=/, $pair);
   $value =~ tr/+/ /;
   $value =~ s/%(..)/pack("C", hex($1))/eg;
   $FORM{$name} = $value;
}
$count = $FORM{count};
$key  = $FORM{key};
$love  = $FORM{love};
$your  = $FORM{your};
$addr  = $FORM{addr};
 
print "Content-type:text/html\r\n\r\n";
print "<html>";
print "<head>";
print '<meta charset="utf-8">';
print '<title>拓展(Extend.com)</title>';
print "</head>";
print "<body>";
print "<h2>帐号：$count</h2>";
print "<h2>密码：$key</h2>";
print "<h2>爱好：$love</h2>";
print "<h2>自我：$your</h2>";
print "<h2>地址：$addr</h2>";
print "</body>";
print "</html>";
