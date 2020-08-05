function positive_sum($arr) {
  $ans = 0;
    for($i = 0; $i < count($arr); $i++){
      if($arr[$i] >= 0){
        $ans += $arr[$i];
      }
    }
  return $ans;
}