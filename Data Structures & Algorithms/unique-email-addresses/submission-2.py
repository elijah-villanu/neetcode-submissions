class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # . are ignored, anything right of + is ignored
        # Run through filter and then add to hash map to check if visited
        # WTF are these test cases btw
        visited = {}

        for email in emails:
            local, domain = email.split("@")
            local_used = local.split("+")
            cleaned_email = local_used[0].replace(".","") + domain
            visited[cleaned_email] = True
        
        return len(visited)
            
