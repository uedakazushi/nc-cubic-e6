# Also support: cd papers && latexmk -lualatex fricke-geometry.tex
use Cwd qw(abs_path);
use File::Basename qw(dirname);
use File::Spec;
my $root_rc = File::Spec->catfile(dirname(dirname(abs_path(__FILE__))), '.latexmkrc');
my $loaded = do $root_rc;
die "Cannot load $root_rc: $@ $!" unless defined $loaded;
