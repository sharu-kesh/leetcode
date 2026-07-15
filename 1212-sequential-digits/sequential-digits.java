class Solution {
    public void findSeq(int low, int high, int num, List<Integer> res){
        if(num >= low && num <= high){
            res.add(num);
        }
        else if(num > high) return;
        int val = num % 10;
        if(val == 9) return;
        num = (num * 10) + (val + 1);
        findSeq(low, high, num, res);
    }
    public List<Integer> sequentialDigits(int low, int high) {
        List<Integer> res = new ArrayList<>();
        for(int i = 1; i < 9; i++){
            findSeq(low, high, i, res);
        }
        Collections.sort(res);
        return res;
    }
}