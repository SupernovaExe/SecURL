import pandas as pd                     # For data transformation
import feature_generation_lexical_function
import urllib

def url_scheme(url):
    scheme_lookup = pd.read_csv('scheme_lookup.csv')
    parsed_url = urllib.parse.urlparse(url)
    parsed_url_scheme = parsed_url.scheme
    try:
        return scheme_lookup[parsed_url_scheme].iloc[0]
    except:
        return 999999


def get_tld(url):
    tld_lookup = pd.read_csv('tld_lookup.csv')
    parsed_url = urllib.parse.urlparse(url)
    tld = parsed_url.netloc.split('.')[-1].split(':')[0]
    try:
        return tld_lookup[tld].iloc[0]
    except:
        return 999999

def lexical_generator(url):

    temp = [[url]]
    url_test = pd.DataFrame(temp, columns=['url'])

    url_test['url_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_length(x))

    url_test['url_domain_entropy'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_domain_entropy(x))

    url_test['url_is_digits_in_domain'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_is_digits_in_domain(x))

    url_test['url_number_of_parameters'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_parameters(x))

    url_test['url_number_of_digits'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_digits(x))

    url_test['url_string_entropy'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_string_entropy(x))

    url_test['url_path_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_path_length(x))

    url_test['url_host_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_host_length(x))

    url_test['get_tld'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.get_tld(x))

    url_test['url_domain_len'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_domain_len(x))

    url_test['url_num_subdomain'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_subdomain(x))

    url_test['url_number_of_fragments'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_fragments(x))

    url_test['url_is_encoded'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_is_encoded(x))

    url_test['url_number_of_letters'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_letters(x))

    url_test['url_num_periods'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_periods(x))

    url_test['url_num_of_hyphens'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_of_hyphens(x))

    url_test['url_num_underscore'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_underscore(x))

    url_test['url_num_forward_slash'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_forward_slash(x))

    url_test['url_num_semicolon'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_semicolon(x))

    url_test['url_num_mod_sign'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_mod_sign(x))

    url_test['has_login_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_login_in_string(x))

    url_test['has_signin_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_signin_in_string(x))

    url_test['has_logon_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_logon_in_string(x))

    url_test['has_loginasp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_loginasp_in_string(x))

    url_test['has_exe_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_exe_in_string(x))

    url_test['has_viewerphp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_viewerphp_in_string(x))

    url_test['has_getImageasp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_getImageasp_in_string(x))

    url_test['has_paypal_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_paypal_in_string(x))

    url_test['has_dbsysphp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_dbsysphp_in_string(x))

    url_test['has_shopping_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_shopping_in_string(x))

    url_test['has_php_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_php_in_string(x))

    url_test['has_bin_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_bin_in_string(x))

    url_test['has_personal_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_personal_in_string(x))

    url_test['url_scheme'] = url_test['url'].apply(lambda x: url_scheme(x))

    url_test = url_test.drop(columns=['url'])

    return url_test