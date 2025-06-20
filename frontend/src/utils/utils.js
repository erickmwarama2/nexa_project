export const formatDate = (ts) =>
  new Date(ts).toISOString().replace("T", " ").slice(0, 19);
