class Solution {
    public int gcdOfOddEvenSums(int n) {
        int sumOdd = 1, sumEven = 2;
        int odd = 1, even = 2;
        n--;
        while(n != 0){
            odd += 2;
            even += 2;
            sumOdd += odd;
            sumEven += even;
            // System.out.println(sumEven + " " + sumOdd);
            n--;
        }
        int gcd = 0;
        while (sumOdd != 0) {
            int temp = sumOdd;
            sumOdd = sumEven % sumOdd;
            sumEven = temp;
        }
        return sumEven;
    }
}