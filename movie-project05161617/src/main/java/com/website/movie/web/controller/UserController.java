package com.website.movie.web.controller;

import com.website.movie.biz.dto.UserDto;
import com.website.movie.biz.model.input.UserInputModel;
import com.website.movie.biz.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

@Controller
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    // SecurityConfig에서 가져옴
//    @Autowired
    private BCryptPasswordEncoder bCryptPasswordEncoder;

//    @GetMapping("/user/gets.api")
//    public List<UserDto> gets() {
//        return userService.gets();
//    }

    @GetMapping("/user")
    public String user() {

        return "user";
    }

    @GetMapping("/login")
    public String login() {

        return "login";
    }
    @GetMapping("/join")
    public String join() {

        return "join";
    }


    @GetMapping("/joinForm")
    public String joinForm() {
        return "joinForm";
    }

    @PostMapping("/join")
    public String join(UserInputModel model) {
        System.out.println(model);
//        model.
        //Security 이용 암호화 코드
        String rawPassword = model.getPassword();
        String encPassword = bCryptPasswordEncoder.encode(rawPassword);
        model.setPassword(encPassword);

        return "redirect:/loginForm";
    }
    // 회원가입 처리
    @PostMapping("/signup")
    public String execSignup(UserDto user) {
        System.out.println(user);
//        List<GrantedAuthority> authorities = new ArrayList<GrantedAuthority>();
//		authorities.add(new SimpleGrantedAuthority("ROLE_ADMIN"));
//        authorities.add(new SimpleGrantedAuthority("ROLE_USER"));
//        user.setAuthorities(authorities);
//        user.setAccountNonExpired(true);
//        user.setAccountNonLocked(true);
//        user.setCredentialsNonExpired(true);
//        user.setEnabled(true);
        user.setCertified(certified_key());
//        userService.createUser(user);
        return "redirect:/user/login";
    }

    private String certified_key() {
        Random random = new Random();
        StringBuffer sb = new StringBuffer();
        int num = 0;

        do {
            num = random.nextInt(75) + 48;
            if ((num >= 48 && num <= 57) || (num >= 65 && num <= 90) || (num >= 97 && num <= 122)) {
                sb.append((char) num);
            } else {
                continue;
            }

        } while (sb.length() < 10);
        return sb.toString();
    }



}
