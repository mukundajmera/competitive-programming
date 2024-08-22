class Solution {
    public boolean backspaceCompare(String s, String t) {
        return checkString(s).equals(checkString(t));
    }

    private String checkString(String word){
        StringBuilder builder = new StringBuilder();
        for(char ch : word.toCharArray()){
            if(ch != '#'){
                builder.append(ch);
            }else if(builder.length() > 0){
                builder.deleteCharAt(builder.length() - 1);
            }
        }
        return builder.toString();
    }
}