class Solution {
    fun pow(x: Double,n:Long):Double{
        //println(n)
        if(n==1L)
            return x
        var a= pow(x,n shr 1)
        var xx=1.0
        if(n and 1==1L)
            xx=x
        return a*a*xx
    }
    fun myPow(x: Double, n: Int): Double {
        if(n==1)
            return x
        var _x=x
        var _n:Long=n.toLong()
        if(n==0)
            return 1.0
        
        if(n<0){
            _x=1.0/x
            _n=n.toLong()
            _n=-_n
        }
            
        return pow(_x,_n)
    }
}