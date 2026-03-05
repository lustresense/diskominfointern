import { Avatar, AvatarFallback } from "@/app/components/ui/avatar";

interface UserAvatarProps {
  name: string;
}

export function UserAvatar({ name }: UserAvatarProps) {
  const initials = name
    .split(" ")
    .map((part) => part[0] || "")
    .join("")
    .slice(0, 2)
    .toUpperCase();

  return (
    <Avatar>
      <AvatarFallback>{initials || "U"}</AvatarFallback>
    </Avatar>
  );
}
