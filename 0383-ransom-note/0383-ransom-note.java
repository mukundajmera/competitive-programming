class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        //create hashmap
        Map<Character, Integer> wordCount = new HashMap<>();
        for(char ch : magazine.toCharArray()){
            wordCount.put(ch, wordCount.getOrDefault(ch,0)+1);
        }

        for(char ch : ransomNote.toCharArray()){
            if(wordCount.get(ch) != null){
                int count = wordCount.get(ch);
                count--;
                if(count == 0){
                    wordCount.remove(ch);
                }else{
                wordCount.put(ch, count);
                }
            }else{
                return false;
            }
        }
        return true;

    }
}