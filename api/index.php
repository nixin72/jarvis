<?php

echo "Hello World";
exit();

$cmd = $_GET["cmd"];
$arg = $_GET["arg"];

echo exec("../jarvis -j $cmd $arg");



?>