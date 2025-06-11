class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        Queue<Integer> q = new LinkedList<>();
        for (int stu:students) q.offer(stu);

        int i = 0;
        int count = 0;
        while(!q.isEmpty() && count < q.size()){
            if(q.peek() == sandwiches[i]){
                i++;
                q.poll();
                count=0;
            }
            else{
                q.offer(q.poll());
                count ++;
            }
        }
        return q.size();
    }
}