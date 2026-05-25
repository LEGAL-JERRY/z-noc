
type Props = {
  status: string
}

export default function StatusBadge({ status }: Props) {
  let className = "status-green"

  if (status === "YELLOW") {
    className = "status-yellow"
  }

  if (status === "RED" || status === "OFFLINE") {
    className = "status-red"
  }

  return (
    <span className={className}>
      {status}
    </span>
  )
}
