@RestController
@RequestMapping("/users")
public class UserController {

    @GetMapping("/info")
    public String getUserInfo() {
        return "User Info from User Service";
    }
}
