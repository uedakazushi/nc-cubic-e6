use Cwd qw(abs_path);
use File::Basename qw(dirname);
use File::Spec;
# Resolve output from this configuration, not from the caller's directory.
my $repo_root = dirname(abs_path(__FILE__));
$pdf_mode = 4;
$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$out_dir = File::Spec->catdir($repo_root, 'build');
$aux_dir = $out_dir;
$max_repeat = 6;
