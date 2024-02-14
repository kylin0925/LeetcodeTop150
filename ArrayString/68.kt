class Solution {

    fun findFarest(idx:Int, words: Array<String>, maxWidth: Int): Pair<Int, Int> {
        var idx = idx
        var cnt = 0
        var wordcnt = 0
        var totalLen=0
        while (idx < words.size){
            var s = if(wordcnt==0) 0 else 1

            if(cnt + words[idx].length + s <= maxWidth){
                cnt+=words[idx].length+s
                totalLen+=words[idx].length
                idx++
                wordcnt++
            }else
                break
        }
        var p = Pair(wordcnt,totalLen)
        return p
    }
    fun addSpace(start:Int, totalLen:Int,wordcnt:Int, words: Array<String>,maxWidth: Int): String {
        var line=""

        if (wordcnt==1 || start + wordcnt == words.size) {
            var l =0
            line = words[start]
            l = words[start].length
            for (i in start+1..start+wordcnt-1) {
                line += " " + words[i]
                l += words[i].length+1
            }
            line += " ".repeat(maxWidth - l)
        }else {
            var spaceCnt = ((maxWidth-totalLen) / (wordcnt - 1)).toInt()
            var rem = (maxWidth-totalLen) % (wordcnt - 1)
            var i = start
            var l = 0
            line = words[i]
            l = words[i].length
            i++
            while (i< words.size && i<start+wordcnt){
                if (rem>0){
                    line+= " ".repeat(spaceCnt+1) + words[i]
                    rem--
                }else{
                    line+= " ".repeat(spaceCnt) + words[i]
                }
                i++
            }
        }
        return line
    }
    fun fullJustify(words: Array<String>, maxWidth: Int): List<String> {
        var ans: ArrayList<String> = ArrayList<String>()
        var cnt = 0
        var wordcnt = words.size
        var i =0
        while (i<wordcnt){
            //find farest word can be put in line
            var (wordcnt,totalLen) = findFarest(i,words,maxWidth)
            var line = addSpace(i,totalLen,wordcnt,words,maxWidth)
            ans.add(line)
            i+=wordcnt
        }
        return ans
    }
}