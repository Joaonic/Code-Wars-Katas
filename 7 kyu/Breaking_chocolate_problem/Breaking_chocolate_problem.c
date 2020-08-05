#include <stdint.h>

uint32_t breaking_chocolate(uint32_t n, uint32_t m){
  if(n > 0){
    if(m > 0){
      return m * n - 1;
    }
  }else{
    return 0;
 }
}