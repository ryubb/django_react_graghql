import { useQuery, gql } from '@apollo/client';
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import Divider from "@material-ui/core/Divider";
import ListItemText from "@material-ui/core/ListItemText";
import ListItemAvatar from "@material-ui/core/ListItemAvatar";
import Avatar from "@material-ui/core/Avatar";
import Typography from "@material-ui/core/Typography";

const EXCHANGE_RATES = gql`
  query User {
    users {
      id, email, name, nameKana, telNumber
    }
  }
`;

const  Users = () => {
  const { loading, error, data } = useQuery(EXCHANGE_RATES);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return data.users.map(({ id, email, name, nameKana, telNumber }: any) => (
    <List key={id}>
      <ListItem alignItems="flex-start">
        <ListItemAvatar>
          <Avatar alt="name" src="/static/images/avatar/1.jpg" />
        </ListItemAvatar>
        <ListItemText
          primary={`${name}(${nameKana})`}
          secondary={
            <>
              <Typography
                component="span"
                variant="body2"
                color="textPrimary"
              >
                {telNumber}
              </Typography>
            </>
          }
        />
      </ListItem>
      <Divider variant="inset" component="li" />
    </List>
  ));
}

export default Users